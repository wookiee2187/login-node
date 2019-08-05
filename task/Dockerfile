FROM centos:7

COPY vc3.repo /etc/yum.repos.d/vc3.repo

RUN rpm --import http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor
RUN curl -L http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo > /etc/yum.repos.d/htcondor-stable-rhel7.repo

RUN yum install epel-release -y
RUN yum install python-pip openssl ansible python-paramiko supervisor minicondor python-devel nginx uwsgi uwsgi-plugin-python2 python-virtualenv -y
RUN yum groupinstall "Development Tools" -y
RUN yum -y install python-pip
RUN pip install kubernetes

# VC3 portal
RUN mkdir -p /srv/www
RUN git clone https://github.com/vc3-project/vc3-website-python /srv/www/vc3-web-env
RUN pushd /srv/www/vc3-web-env  && \
     virtualenv venv && source venv/bin/activate && \
     pip install -r requirements.txt && \
     popd
RUN pushd /srv/www/vc3-web-env && \
     virtualenv venv && source venv/bin/activate && \
     git clone https://github.com/vc3-project/vc3-infoservice && \
     pushd vc3-infoservice && \
       git fetch --tags && \
       git checkout v1.1.0 && \
       python setup.py install && \
     popd && \
     git clone https://github.com/vc3-project/vc3-client && \
     pushd vc3-client && \
       git fetch --tags && \
       git checkout v1.1.0 && \
       python setup.py install && \
     popd && \
   popd

# OpenStack provisioning - remove when obsolete
RUN yum install centos-release-openstack-ocata python-novaclient -y

RUN yum install vc3-infoservice pluginmanager openssl vc3-client vc3-master \
    pluginmanager vc3-playbooks autopyfactory vc3-factory-plugins \
    vc3-remote-manager vc3-builder credible -y
RUN pip install pyOpenSSL CherryPy==3.2.2

# OpenStack provisioning
RUN yum install centos-release-openstack-ocata python-novaclient -y

COPY credible.conf /etc/credible/credible.conf

RUN credible -c /etc/credible/credible.conf hostcert localhost > /etc/pki/tls/certs/hostcert.pem
RUN credible -c /etc/credible/credible.conf hostkey localhost > /etc/pki/tls/private/hostkey.pem
RUN credible -c /etc/credible/credible.conf certchain > /etc/pki/ca-trust/extracted/pem/vc3-chain.cert.pem


COPY vc3-infoservice.conf /etc/vc3/vc3-infoservice.conf
COPY vc3-master.conf /etc/vc3/vc3-master.conf
COPY vc3-client.conf /etc/vc3/vc3-client.conf
COPY tasks.conf /etc/vc3/tasks.conf

RUN mkdir -p /var/log/vc3
RUN chown vc3: /var/log/vc3
RUN mkdir -p /var/credible/ssh
RUN chown vc3: /var/credible/ssh
RUN mkdir -p /var/log/autopyfactory
RUN chown autopyfactory: /var/log/autopyfactory

# systemctl start vc3-master

COPY vc3defaults.conf /etc/autopyfactory/vc3defaults.conf
COPY autopyfactory.conf /etc/autopyfactory/autopyfactory.conf
COPY monitor.conf /etc/autopyfactory/monitor.conf
COPY auth.conf /etc/autopyfactory/auth.conf
COPY vc3.ini /etc/uwsgi.d/vc3.ini
COPY uwsgi_params /etc/nginx/uwsgi_params
COPY nginx.conf /etc/nginx/nginx.conf

# This is very strange. APF is not inheriting its environment or something
RUN chown autopyfactory: /root
RUN chmod 755 /root

# Should be temporary til a real cert is in place
RUN mkdir -p /etc/nginx/certificate/
RUN openssl req -newkey rsa:2048 -nodes -keyout /etc/nginx/certificate/www-dev.virtualclusters.org.key \
    -x509 -days 180 -out /etc/nginx/certificate/www-dev.virtualclusters.org.pem \
    -subj "/C=US/ST=Illinois/L=Chicago/O=University of Chicago/CN=localhost"

#service condor start
#service autopyfactory start

COPY supervisord.conf /etc/supervisord.conf

# Load the standard values into the infoservice
#RUN /srv/www/vc3-web-env/vc3-client/testing/standard-loadinfo.sh

EXPOSE 80/tcp
EXPOSE 443/tcp

ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf"]
