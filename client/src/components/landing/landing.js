import React from 'react'
import Slideshow from './Slideshow'

import './Landing.scss'

const Landing = () => {
    return (
        <div className='Landing'>
            {/* <Slideshow /> */}
            <div className='Landing__Container'>
                <div className='Landing__Mission'>
                    <h5>Our Mission to the Community</h5>
                    <ul>
                        <li>Increase voter turnout</li>
                        <li>Build community connections among neighbors</li>
                        <li>Use metrics to inspire action and measure results</li>
                        <li>Provide opportunities for partnerships and synergies</li>
                        <li>Encourage inclusion and trust</li>
                    </ul>
                </div>
                <div className='Landing__Founder'>
                    <h5>How we came to be</h5>
                </div>
            </div>
        </div>
    )
}

export default Landing
