import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/navbar/navbar'
import Landing from './components/landing/landing'
import Voting from './components/voting/voting'
import Calendar from './components/calendar/events'
import Social from './components/social/social'
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
