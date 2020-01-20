import React from 'react';
import './LandingPage.scss';
import { Link } from 'react-router-dom';

const LandingPage: React.FC = () => (
    <article className="landingpage">
        <h1 className="landingpage__headline">Categories:</h1>
        <div>
            <Link to="/" className="landingpage__link"><span>Gaming</span></Link>
            <Link to="/" className="landingpage__link"><span>News</span></Link>
        </div>
    </article>
);

export default LandingPage;
