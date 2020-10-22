import React from 'react'
import './Voting.scss'

const Voting = () => {
    return (
        <div className='Voting'>
            <div className='Voting__Info'>
                <h5>Voting Locations</h5>
                <p>Polling Locations open from 7am - 7pm</p>
                <img src='/images/map.png' alt='Voting Areas'/>
                <ul>
                    <li>Bethel Metropolitan Baptist Church - 2455 26th Ave. S.</li>
                    <li>Gulfport Hity Hall - 2401 53rd St. S.</li>
                    <li>Gulfport Recreation Center - 5730 Shore Blvd. S.</li>
                    <li>Gulfport Neighborhood Center - 1617 49th St. S.</li>
                    <li>Lions Club of Golfport - 4630 Tifton Dr. S.</li>
                </ul>
            </div>
            <div className='Voting__Ballot'>
                <h5>Gulfport Sample Ballot</h5>
                <img src="/images/ballot1.jpg" alt="Sample Ballot"/>
                <img src="/images/ballot2.jpg" alt="Sample Ballot"/>
                <img src="/images/ballot3.jpg" alt="Sample Ballot"/>
            </div>
        </div>
    )
}

export default Voting
