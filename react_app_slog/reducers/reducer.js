function reducer(state={
        total_msg:[] 
    }, action){
    console.log("in reducer:",action.type)
    switch(action.type){
        case 'fetched':
            return {
                total_msg: action.total_msg
            }
        default: 
            return state;
    }
}

export default reducer;
