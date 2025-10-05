from flask import Flask,request,jsonify
import json
import os

stu=Flask(__name__)
Stu_data='application.json'

def data_display():
    if not os.path.exists(Stu_data) or os.path.getsize(Stu_data)==0:# to chk if file is empty of not created
        return []
    try:
        with open(Stu_data,'r') as s:
            return json.load(s)
    except json.JSONDecodeError:# if file is corrupt
        return []
        
def data_add(data):
    with open(Stu_data,'w') as s:
        json.dump(data,s,indent=3)# for separating data indent
        
@stu.route('/',methods=['GET'])
def home():
    return jsonify({"message":"Routine check,endpoint for documentation"}),200#indicates status is okay
    
@stu.route('/apply',methods=['POST'])
def sub_data():
    data=request.get_json()
    req_fields=['Name','r_n','Dept','Sec','Intr']
    if not data or not all(field in data for field in req_fields):# if true returned error hence will go in loop
        return jsonify({"error":"Missing required fields...."+",".join(req_fields)}), 400# data now comma separated 400-bad request
    app=data_display()
    new_id = max((a.get('ID', 0)for a in app),default=0)+1# for getting unique index
    new_app={
        'ID':new_id,
        'Name':data['Name'],
        'Roll_no':data['r_n'],
        'Department':data['Dept'],
        'Section':data['Sec'],
        'Intrests':data['Intr']
    }
    app.append(new_app)
    data_add(app)
    return jsonify({"message":"Application submitted successfully","application":new_app}), 201# create chr code

@stu.route('/application',methods=['GET'])# chk 
def read_all_data():
    app=data_display()
    return jsonify(app),200
    
@stu.route('/application/<int:stu_id>',methods=['GET'])# chk
def read_specific_data(stu_id):
    apps=data_display()
    data=next((a for a in apps if a.get('ID')==stu_id), None)#next-finds first match,None if no id found
    if data==None:
        return jsonify({"error":f"Application with ID {stu_id} not found"}),404#Error
    return jsonify(data),200
    
@stu.route('/application/<int:stu_id>',methods=['DELETE'])
def delete_application(stu_id):
    apps=data_display()
    c_i=len(apps)
    updated_applications=[a for a in apps if a.get('ID')!=stu_id]
    if len(updated_applications)==c_i:
        return jsonify({"error":f"Application with ID {stu_id} not found"}),404
    data_add(updated_applications)
    return jsonify({'message':f'Application with ID {stu_id}successfully deleted'}),200
    
if __name__ == '__main__':
    if not os.path.exists(Stu_data) or os.path.getsize(Stu_data)==0:
        data_add([])    
    stu.run(debug=True, port=5000)




    
    
