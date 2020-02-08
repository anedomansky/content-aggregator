import React from 'react';
import './Footer.scss';

const Footer: React.FC = () => (
    <footer role="contentinfo">
        <p>
            &copy;
            {` ${new Date().getFullYear()}`}
        </p>
    </footer>
);

export default Footer;
