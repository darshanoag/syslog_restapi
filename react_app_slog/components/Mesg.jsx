import store from "../stores/store.js";
import fetchtotalmsg from "../rest/ajax.js";
import React from "react";

class Mesg extends React.Component {
    constructor(props) {
        super(props);
        store.subscribe(()=>{
           this.forceUpdate();
        });
        this.state = {
            total_msg: undefined,
            total_err_msg: undefined
        }
        console.log("Message is subscribing");
        this.state.total_msg = fetchtotalmsg() 
        console.log("line:17",store.getState())
   }

   render() {
       return (
           <div>
                <button type="button" onClick={() => this.setState({total_msg: fetchtotalmsg()})}>Total number of messages:</button>
                 {store.getState().total_msg}
                <br />
           </div>
           );
   }
}

export default Mesg; 
