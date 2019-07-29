from pyhelm.chartbuilder import ChartBuilder
from pyhelm.tiller import Tiller

chart = ChartBuilder({"name": "login-node", "source": {"type": "git", "location": "https://github.com/slateci/slate-catalog/tree/master/incubator/login-node/login-node"}})
chart.get_metadata()
#tiller.install_release(chart.get_helm_chart(), dry_run=False, namespace='default')
