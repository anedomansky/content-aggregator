import React from 'react';
import { Link } from 'react-router-dom';
import './NotFoundPage.scss';

const NotFoundPage: React.FC = () => (
    <article className="not-found-page">
        <h1>Sorry, page not found</h1>
        <h4>
            Return to the
            <Link to="/" className="not-found-page__link"> landing page</Link>
        </h4>
    </article>
);

export default NotFoundPage;
