import React, {useState, useEffect} from 'react';
import './Landing.scss';

const Slideshow = () => {
    const [curImage, setCurImage] = useState (0)
    const images = ['/images/slideshow/slideshow1.webp', '/images/slideshow/slideshow2.webp','/images/slideshow/slideshow3.webp', '/images/slideshow/slideshow4.webp', '/images/slideshow/slideshow5.webp', '/images/slideshow/slideshow6.webp']

    const goToNext = () => {
        setCurImage(curImage === images.length - 1 ? 0 : curImage + 1);
    }

    // useEffect(() => {
    //     setTimeout(goToNext, 3000);
    //     console.log(curImage);
    //     return () => {
    //         clearTimeout(goToNext);
    //     };
    // });

    return (
        <div className="Slideshow">
            {images.map((image, key) => (
                <div className={key === curImage ? "Slideshow__Images Active" : "Slideshow__Images"} key={key}>
                    {key === curImage && (
                        <img src={`${image}`} alt="Gulfport Votes Images" />
                    )}
                </div>
            ))}
        </div>
    );
}

export default Slideshow
