FROM centos:latest 

RUN \
  yum update -y && \
  yum install -y epel-release

RUN \
  yum install -y openssh-server pwgen supervisor

RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' \
&& ssh-keygen -t dsa  -f /etc/ssh/ssh_host_dsa_key -N '' \
&& ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' \
&& chmod 600 /etc/ssh/*

RUN \
  sed -i -r 's/.?UseDNS\syes/UseDNS no/' /etc/ssh/sshd_config && \
  sed -i -r 's/.?PasswordAuthentication.+/PasswordAuthentication no/' /etc/ssh/sshd_config && \
  sed -i -r 's/.?ChallengeResponseAuthentication.+/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config && \
  sed -i -r 's/.?PermitRootLogin.+/PermitRootLogin no/' /etc/ssh/sshd_config

RUN \
  sed -ri 's/^HostKey\ \/etc\/ssh\/ssh_host_ed25519_key/#HostKey\ \/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config && \
  sed -ri 's/^#HostKey\ \/etc\/ssh\/ssh_host_dsa_key/HostKey\ \/etc\/ssh\/ssh_host_dsa_key/g' /etc/ssh/sshd_config && \
  sed -ri 's/^#HostKey\ \/etc\/ssh\/ssh_host_rsa_key/HostKey\ \/etc\/ssh\/ssh_host_rsa_key/g' /etc/ssh/sshd_config && \
  sed -ri 's/^#HostKey\ \/etc\/ssh\/ssh_host_ecdsa_key/HostKey\ \/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config && \
  sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN \
  echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config

RUN \
  echo > /etc/sysconfig/i18n

RUN \
  yum clean all && rm -rf /tmp/yum*

ADD container-files /

ENTRYPOINT ["/config/bootstrap.sh"]
