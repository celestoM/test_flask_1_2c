from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def main():
    return {"payload":"welcome to my project "}


@app.route("/read")
def read():
    leer=request.args.get("content")
    if leer=="foo":
        return {"payload":leer}
    else:
        return "Usuario No Existe"
    

@app.route("/create", methods=["POST"])
def create():
    leer=request.args.get("content")
    if leer=="bar":
        return {"payload":leer}
    else:
        return "Usuario No Existe"
    
@app.route("/delete", methods=["DELETE"])
def delete():
    leer=request.args.get("content")
    if leer=="qux":
        return {"payload":leer}
    else:
        return "Usuario No Existe"  


@app.route("/put", methods=["PUT"])
def put():
    leer=request.args.get("content")
    if leer=="echo":
        return {"payload":leer}
    else:
        return "Usuario No Existe"  


@app.route("/init", methods=["GET"])
def init():
    leer=request.args.get("content")
    if leer=="alfa":
        return {"payload":leer}
    else:
        return "Usuario No Existe"




if __name__ == "__main__":
    app.run(debug=True)
