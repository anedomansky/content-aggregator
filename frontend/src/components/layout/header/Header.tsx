import React from 'react';
import './Header.scss';
import { Link } from 'react-router-dom';

// TODO: style with home icon on hover - transform: translateY(300%) not working?
const Header: React.FC = () => (
    <header>
        <Link to="/" className="title">
            <span>Content-Aggregator</span>
        </Link>
    </header>
);

export default Header;
