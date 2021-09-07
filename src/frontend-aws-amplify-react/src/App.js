import logo from './logo.svg';
import './App.css';


import React, { Component } from 'react';



var callAPI = (firstName,lastName)=>{
  // instantiate a headers object
  var myHeaders = new Headers();
  // add content type header to object
  myHeaders.append("Content-Type", "application/json");
  // using built in JSON utility package turn object to string and store in a variable
  var raw = JSON.stringify({"firstName":firstName,"lastName":lastName});
  // create a JSON object with parameters for API call and store in a variable
  var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
  };
  // make API call with parameters and use promises to get response
  fetch("https://67nbvuy3t1.execute-api.us-east-2.amazonaws.com/dev/", requestOptions)
  .then(response => response.text())
  .then(result => alert(JSON.parse(result).body))
  .catch(error => console.log('error', error));
}















class App extends React.Component {
  render() { 
    return (
      <div className="App">
        <form>
            <label>First Name :</label>
            <input type="text" id="fName"/>
            <label>Last Name :</label>
            <input type="text" id="lName"/>
            <button type="button" onclick="{callAPI(document.getElementById('fName').value,document.getElementById('lName').value)}">Call API</button>
        </form>
      </div>
    );
  }
}
 
export default App;





