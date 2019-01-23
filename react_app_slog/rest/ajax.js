import store from '../stores/store.js';

function fetchtotalmsg() {
    console.log("calling RestAPI")
    return fetch('http://bgl-ads-523:5000/total_msg').then(function(response){
            return response.json();
        }).then(function(data){
            store.dispatch({
                type: 'fetched',
                total_msg: data.total_msg
            });
        
        });
};

export default fetchtotalmsg;
