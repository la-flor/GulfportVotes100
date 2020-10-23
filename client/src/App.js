import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar'
import Landing from './components/Landing/Landing'
import Voting from './components/Voting/Voting'
import Calendar from './components/Calendar/Events'
import Social from './components/Social/Social'
import Admin from './components/Admin/Admin'
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
          <Route path='/admin' children={<Admin />} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
