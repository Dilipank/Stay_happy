import React, { Component } from 'react';
import './App.css';
import InputTextBox from './components/inputBox';
import InputButton from './components/clbutton';

import CalenderPick from './components/calenderPick';
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <InputTextBox />
          <CalenderPick />
          <CalenderPick />
        
          <InputButton name="Search"/>
        </header>
      </div>
    );
  }
}

export default App;
