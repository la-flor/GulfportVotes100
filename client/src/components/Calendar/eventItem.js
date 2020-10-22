import React from 'react'
import './Events.scss'

const EventItem = ({title, description}) => {
    return (
        <div className='Events__Item'>
            <h5>{title}</h5>
            <p>{description}</p>
        </div>
    )
}

export default EventItem
