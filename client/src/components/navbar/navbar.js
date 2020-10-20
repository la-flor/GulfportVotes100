import React from 'react'
import { Link } from 'react-router-dom';
import './navbar.scss'

const navbar = () => {
    return (
        <div className='Navbar'>
            <div className='Navbar__Name'>
                <img src="/images/logo.jpg" alt="Logo"/>
                <Link to='/'>
                    <h5>Gulport Votes 100%</h5>
                </Link>
            </div>
            <ul className='Navbar__Links'>
                <Link to='/voting'>
                    <li>Voting</li>
                </Link>
                <Link to='/calendar'>
                    <li>Events</li>
                </Link>
                <Link to='/social'>
                    <li>Social</li>
                </Link>
            </ul>
        </div>
    )
}

export default navbar
