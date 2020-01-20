import React from 'react';
import './Footer.scss';

const Footer: React.FC = () => (
    <footer>
        <p>
            &copy;
            {` ${new Date().getFullYear()}`}
        </p>
    </footer>
);

export default Footer;
