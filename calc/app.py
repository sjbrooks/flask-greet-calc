from flask import Flask, request
app = Flask(__name__)


from operations import add, sub, mult, div
# Do we need these variables or just if we # want to rename the function in this file?
# add = add(a,b)
# sub = sub(a,b)
# mult = mult(a,b)
# div = div(a,b)


OPERATIONS = {
	"add": add,
	"sub": sub,
	"mult": mult,
	"div": div
}

@app.route("/math/<operation>")
def math(operation):

	math_operation = OPERATIONS[operation]

	a = int(request.args.get("a"))
	b = int(request.args.get("b"))

	return str(math_operation(a, b))


@app.route("/add")
def add_operation():
	"""Handle get request and add a and b params"""
	a = int(request.args.get("a"))
	b = int(request.args.get("b"))

	return str(add(a,b))

@app.route("/sub")
def sub_operation():
	"""Handle get request and subtract b from a"""

	a = int(request.args.get("a"))
	b = int(request.args.get("b"))

	return str(sub(a, b))

@app.route("/mult")
def mult_operation():
	"""Handle get request and multiply a and b params"""

	a = int(request.args.get("a"))
	b = int(request.args.get("b"))

	return str(mult(a, b))

@app.route("/div")
def div_operation():
	"""Handle get request and divide a by b"""

	a = int(request.args.get("a"))
	b = int(request.args.get("b"))

	return str(div(a, b))

