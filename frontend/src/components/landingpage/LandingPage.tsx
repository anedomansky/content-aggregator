import React from 'react';
import './LandingPage.scss';
import { Link } from 'react-router-dom';

const LandingPage: React.FC = () => (
    <article className="landing-page">
        <h1 className="landing-page__headline">Categories:</h1>
        <div>
            <Link to="/gaming" className="landing-page__link"><span>Gaming</span></Link>
            <Link to="/news" className="landing-page__link"><span>News</span></Link>
        </div>
    </article>
);

export default LandingPage;
