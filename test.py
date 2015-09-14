import util
def new_dict_test():
	dict = {"name":"linzhixiong","age":10,"score":100}
	fileds =["name","score"]
	assert cmp(util.new_dict(fileds,dict),{"name":"linzhixiong","score":100}) == 0