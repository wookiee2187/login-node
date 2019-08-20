from jinja2 import Environment, FileSystemLoader

#env = Environment(loader = FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
{% set request_name = "request.name"}
template = env.get_template('deployNservice.yaml')
temp_up = template.render(config_data)
