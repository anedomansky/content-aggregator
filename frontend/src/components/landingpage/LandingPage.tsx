import React from 'react';
import './LandingPage.scss';
import { Link } from 'react-router-dom';

const LandingPage: React.FC = () => (
    <article>
        <h2>Categories:</h2>
        <h3>
            <Link to="/">Gaming</Link>
        </h3>
        <h3>
            <Link to="/">News</Link>
        </h3>
    </article>
);

export default LandingPage;
