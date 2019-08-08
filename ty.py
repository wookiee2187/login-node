import cur_yaml

data = dict(
    A = 'a',
    B = dict(
        C = 'c',
        D = 'd',
        E = 'e',
    )
)

with open('yt.yml', 'r') as outfile:
    cur_yaml = yaml.safe_load(outfile)
    cur_yaml.update(data)
    print(cur_yaml)

