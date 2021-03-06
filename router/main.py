from flask import Flask, jsonify, request
from flask import Blueprint
from werkzeug.utils import secure_filename
from datetime import datetime
import certifi

SECRET_KEY = '$lucky7'

# DB 연결 코드
from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://luckyseven:luckyseven@cluster0.2hyld.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
    tlsCAFile=certifi.where())
db = client.od_project

bp = Blueprint("main", __name__, url_prefix="/main")

@bp.route('/api/img/upload', methods=['POST'])
def file_upload():
    # 업로드 파일 받아오기.
    file = request.files['file'] # werkzeug.datastructures.FileStorage, name
    extension = secure_filename(file.filename).split('.')[-1] # file.filename /
    f_name = file.filename.replace('.' + extension, '') # test1, 확장자 제거

    # 파일 이름 , Local에 Upload 한 이미지 저장
    today = datetime.now()
    today = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f_name + '-' + today # test1-2022-05-19-14-43-23.jpg
    upload_path = 'static/upload_data/' + filename + '.' + extension
    file.save(upload_path) # 'static/upload_data/test1.jpg

    # user 정보 
    user_id = request.form["user_id"]
    user_name = request.form["user_name"]
    user_company = request.form["user_company"]
    file_type = request.form["file_type"]
    
    # DB에 Upload Path 저장
    doc = {
        'id': user_id,
        'name': user_name,
        'num': 0,
        'company': user_company,
        'file_type': file_type,
        'helmet': None,
        'head': None,
        'score': None,
        'isPass': None,
        'date': today,
        'upload_path': upload_path,
        'predict_path': None
    }
    db.RESULT.insert_one(doc)
    return jsonify({'result':'success', 'upload_path':upload_path, 'msg': '업로드가 완료 되었습니다.'})

@bp.route("/api/video/upload", methods=['POST'])
def video_upload():
    file = request.files['file']  # print(file) # 전체적인 파일의 개요 확인
    extension = secure_filename(file.filename).split('.')[-1]  # file.filename /
    f_name = file.filename.replace('.' + extension, '')  # test1, 확장자 제거

    # 파일 이름 , Local에 Upload 한 이미지 저장
    today = datetime.now()
    today = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f_name + '-' + today  # test1-2022-05-19-14-43-23.jpg
    upload_path = 'static/upload_data/' + filename + '.' + extension
    file.save(upload_path)  # 'static/upload_data/test1.jpg

    # user 정보 
    user_id = request.form["user_id"]
    user_name = request.form["user_name"]
    user_company = request.form["user_company"]
    file_type = request.form["file_type"]

    # DB에 Upload Path 저장
    doc = {
        'id': user_id,
        'name': user_name,
        'num': 0,
        'company': user_company,
        'file_type': file_type,
        'helmet': None,
        'head': None,
        'score': None,
        'isPass': None,
        'date': today,
        'upload_path': upload_path,
        'predict_path': None
    }
    db.RESULT.insert_one(doc)
    return jsonify({'result':'success', 'upload_path':upload_path, 'msg': '업로드가 완료 되었습니다.'})
