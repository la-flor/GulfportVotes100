import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar'
import Landing from './components/Landing/Landing'
import Voting from './components/Voting/Voting'
import Calendar from './components/Calendar/Events'
import Social from './components/Social/Social'
import './App.scss';

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Switch>
          <Route exact path='/' children={<Landing />} />
          <Route path='/voting' children={<Voting />} />
          <Route path='/calendar' children={<Calendar />} />
          <Route path='/social' children={<Social />} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
