# This is just a simple craler must run asa separte provcess - Dipankar



from flask import Flask, request
import pickle
import pdb
import json





##################  INIT DATABASE ############################
import database
store = database.Store(); #return single ton..

###############################################################





###############  Multi thread to get the data ##############
import threading
import crawler
def schedule():
    # do something here ...
    print '*'*50
    print 'Running Scheduler....'
    import time
    print 'Time:', time.ctime() # 'Mon Oct 18 13:35:29 2010'
    print '*'*50
    crawler.UpdateDataBase();
    print '*'*50
    # call f() again in 60 seconds
    threading.Timer(60*60*4, schedule).start() #Run every 4 hours
###############################################################



##########################  We server ################################
from flask import Flask, Response
app = Flask(__name__)

@app.route('/news')
def hello_world():
    try:
        #pdb.set_trace();
        page = 1   if not request.args.get('page') else int(request.args.get('page') )
        limit = 50 if not request.args.get('limit') else int(request.args.get('limit') )
        query = '' if not request.args.get('query') else request.args.get('query')

        global store
        result =[]
        if len(query.strip()) == 0:
            result = store.get(page, limit)
        else:
            result = store.getByCat(query, page, limit)

        return Response(json.dumps({'result':result}), mimetype ='application/json')
            
    except Exception,e:
       print e
       return Response(json.dumps({'result':[],'status':'error','msg':'Somethong goes wrong ! Talk to dipankar!'+str(e)}), mimetype ='application/json')
#########################################################################       

if __name__ == '__main__':
    schedule()
<<<<<<< HEAD
=======
    #app.run(host='0.0.0.0', port=5555, debug=True,threaded=True)
>>>>>>> 28757c2b01fbbdab4d576e9468598482c30da5ba
