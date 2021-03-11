import React from 'react';
import './Events.scss';

const EventItem = ({ id, title, description, scheduled_time }) => {
	return (
		<div id={id} className='Events__Item'>
			<h5>{title}</h5>
			<p>{scheduled_time}</p>
			<p>{description}</p>
		</div>
	);
};

export default EventItem;
