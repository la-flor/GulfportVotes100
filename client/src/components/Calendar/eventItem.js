import React from 'react'
import './events.scss'

const eventItem = ({title, description}) => {
    return (
        <div className='Events__Item'>
            <h5>{title}</h5>
            <p>{description}</p>
        </div>
    )
}

export default eventItem
