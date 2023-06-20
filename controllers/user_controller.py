from app import app
from models.user_model import user_model
from flask import request

obj = user_model()

@app.route('/user/getall')
def user_getall_model():
    return obj.user_getall_model()


@app.route('/user/add', methods=['POST'])
def user_addone_controller():
    return obj.user_addone_model(request.form)


@app.route('/user/update', methods=['PUT'])
def user_update_controller():
    return obj.user_update_model(request.form)


@app.route('/user/delete/<int:id>', methods=['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)