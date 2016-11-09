from flask import Flask, abort, request
import json

from files_commands import get_all_files, add_file, remove_file

app = Flask(__name__)

api_url = '/recently_created'

@app.route('/files',methods=['POST'])
def create_file():
  content = request.get_json(silent=True)
  filename = content['filename']
  content =  content['content']
  add_file(filename,content)  
  return "Se creo",201
  

@app.route('/files',methods=['GET'])
def read_file():
  list = {}
  list["files"] = get_all_files()
  return json.dumps(list), 200

@app.route('/files',methods=['PUT'])
def update_file():
  return "not found", 404

@app.route('/files',methods=['DELETE'])
def delete_file():
  error = False
  for username in get_all_files():
    if not remove_file(filename):
        error = True

  if error:
    return 'some files were not deleted', 400
  else:
    return 'all files  were deleted', 200  	 

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
