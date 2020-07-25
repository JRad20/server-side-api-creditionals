from flask import Flask, jsonify, request
import json
import pymongo
import logging

# http://127.0.0.1:5000/authenticate

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True


@app.route('/authenticate',methods=['GET','POST'])
def index():

    if request.method == 'POST':

        """ 
        Example of getting data from the post
        
        get_data = request.form.to_dict(flat=False)
        data = get_data['key']
        make_str = str(data)
        remove_list = make_str[:-2]
        remove_list2 = remove_list[2:]
        key = remove_list2
        
        """

        """
        Example with connecting to mongo and finding a users licence

        DATABASE = "database"
        CONNECTION_STRING = "your_connection_url"
        client = pymongo.MongoClient(CONNECTION_STRING)
        client.server_info()
        db = client[DATABASE]
        collection = db["your_collection"]
        """
        
        """ 
        Example of trying to find key out of data base
        try:
            result = collection.find({"key": key})
            user = result[0]
            user_license = user['key']
        """

         
            """ 
            Example of checking to see if the key is active inside my database please modify for your own needs
         
            check_active_status = user['active']
            active_status = str(check_active_status)
            
             """ 

            """
            checking to see if the key is already activated / invalid and updating the key to valid

            if active_status == 'True':
                get_uuid = user['uuid']
                uuid = str(get_uuid)
                if uuid == device_id:
                    return '200'
                else:
                    return 'key is already active'
            if active_status == 'False':
                collection.update_one({'_id': user['_id']}, {'$set': {'active': True}})
                return '200'


        except:
            return '403'
             """
    

    if request.method == 'GET':
        return 'GET is not a valid request method!'
     # return nothing if get requests



if __name__ == '__main__':
    app.run(debug=False)
