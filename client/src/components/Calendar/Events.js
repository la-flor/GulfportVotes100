import React from 'react';
import EventItem from './EventItem';
import './Events.scss';

const Events = () => {
	return (
		<div className='Events'>
			<div className='Events__List'>
				<EventItem
					title='Nov 3rd: ComeUnity Celebration'
					description='Shake off the election stress and have some fun with your neighbors and friends'
				/>
				<EventItem
					title='Oct 24th: Drive in Movie Night'
					description='Join us in watching "All In: The Fight for Democracy", a riveting examination of voter suppression in the United States'
				/>
				<EventItem
					title='Oct 22nd: National Voter Registration Day'
					description='If you have not registered yet, today is the day!'
				/>
				<EventItem
					title='Oct 9th: Porch Party'
					description='A free, family-friendly outdoor party celebrating Volunteers and Voting.'
				/>
				<EventItem
					title='Oct 6th: Florida Registration Day'
					description="Florida's official registration day. Don't delay! Register today!"
				/>
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
