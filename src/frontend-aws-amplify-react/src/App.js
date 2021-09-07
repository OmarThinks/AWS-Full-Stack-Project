import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <form>
          <label>First Name :</label>
          <input type="text" id="fName"/>
          <label>Last Name :</label>
          <input type="text" id="lName"/>
          <button type="button" onclick="">Call API</button>
      </form>
    </div>
  );
}

export default App;
