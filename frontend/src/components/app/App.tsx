import React from 'react';
import { renderRoutes } from 'react-router-config';
import routes from '../../routes';
import './App.scss';
import Header from '../layout/header/Header';
import Footer from '../layout/footer/Footer';

const App: React.FC = () => (
    <div className="content" role="application">
        <Header />
        <main role="main">
            {renderRoutes(routes)}
        </main>
        <Footer />
    </div>
);

export default App;
