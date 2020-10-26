import React, { useState, useEffect, useCallback } from 'react';
import './Landing.scss';

const Slideshow = () => {
	const [curImage, setCurImage] = useState(0);
	const images = [
		'/images/slideshow/slideshow1.jpg',
		'/images/slideshow/slideshow2.jpg',
		'/images/slideshow/slideshow3.jpg',
		'/images/slideshow/slideshow4.jpg',
		'/images/slideshow/slideshow5.jpg',
		'/images/slideshow/slideshow6.jpg',
	];

	const goToNext = useCallback(() => {
		setCurImage(curImage === images.length - 1 ? 0 : curImage + 1);
	}, [images.length, curImage]);

	useEffect(() => {
		setTimeout(goToNext, 4000);
		return () => {
			clearTimeout(goToNext);
		};
	}, [goToNext]);

	return (
		<div className='Slideshow'>
			<div className='Slideshow__Background'>
				{images.map((image, key) => (
					<div
						key={key}
						className={
							key === curImage
								? 'Slideshow__Images Active'
								: 'Slideshow__Images'
						}>
						{key === curImage && (
							<img src={`${image}`} alt='Gulfport Votes Images' />
						)}
					</div>
				))}
			</div>
		</div>
	);
};

export default Slideshow;
