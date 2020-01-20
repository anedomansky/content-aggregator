import React from 'react';
import './Header.scss';
import { Link } from 'react-router-dom';

// TODO: style with home icon on hover - transform: translateY(300%) not working?
const Header: React.FC = () => (
    <header>
        <h3 className="title"><Link to="/"><span>Content-Aggregator</span></Link></h3>
    </header>
);

export default Header;
