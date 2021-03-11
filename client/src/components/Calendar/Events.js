import React, { useState, useEffect } from 'react';
import EventItem from './EventItem';
import axios from 'axios';

import './Events.scss';

const Events = () => {
	const REACT_APP_API_URL = "http://localhost:5000";
	const [events, setEvents] = useState([])

	useEffect(function loadEvents() {
		try {
			async function getEventInfo() {
				const { data } = await axios.get(`${REACT_APP_API_URL}/events`)
				setEvents(data.events)
			}
			getEventInfo()
		} catch (err) {
			console.error("Unable to load events from server.", err)
		}
	}, [])

	return (
		<div className='Events'>
			<div className='Events__List'>
				{events.length 
					? (events.map(e => 
							<EventItem 
								key={e.id} 
								id={e.id} 
								title={e.title} 
								description={e.description}
								scheduled_time={e.scheduled_time.slice(5,16)} />))
					: <h3>There are no future events currently scheduled.</h3>}
			</div>
			<div className='Events__Calendar'>
				<iframe
					src='https://calendar.google.com/calendar/embed?height=400&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=America%2FDenver&amp;src=NGI3a3RjYnF2cWVkOTY0aTExN3FzbWRraXNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;src=ZW4udXNhI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&amp;color=%23C0CA33&amp;color=%230B8043&amp;showNav=1&amp;showTabs=0&amp;showPrint=0&amp;showDate=1&amp;showCalendars=0&amp;title=Gulfport%20Votes%20100%25'
					frameBorder='0'
					scrolling='no'
					title='calendar'></iframe>
			</div>
		</div>
	);
};

export default Events;
