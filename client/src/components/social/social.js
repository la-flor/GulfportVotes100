import React from 'react'
import './Social.scss'

const Social = () => {
    return (
        <div className='Social'>
            <div className='Social__Image'>
                <img src="/images/social.jpg" alt="Social"/>
            </div>
            <div className='Social__Contact'>
                <div className='Social__Facebook'>
                    <a href="https://www.facebook.com/GulfportVotes100/?ref=page_internal">
                        <h4>Facebook</h4>
                    </a>
                    <h5>Reach out to us on Facebook if you have any questions</h5>
                </div>
                <div className='Social__News'>
                    <h4>Gulfport Votes 100% in the News</h4>
                    <a className='Social__Gabber' href="https://thegabber.com/search/votes+100/">
                        <p>The Gabber</p>
                    </a>
                    <ul>
                        <a href="https://thegabber.com/gulfport-votes-100-unveils-local-art/">
                            <li>Gulfport Votes 100% Unveils Local Art</li>
                        </a>
                        <a href="https://thegabber.com/gulfport-votes-100-spreads-the-word/">
                            <li>Gulfport Votes 100% Spreads the Word </li>
                        </a>
                        <a href="https://thegabber.com/local-group-aims-for-100-voter-turnout/">
                            <li>Local Group Aims For 100% Voter Turnout</li>
                        </a>
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default Social
