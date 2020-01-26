import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import List from '../common/List';
import './GamingPage.scss';
import { IStories } from '../../interfaces/IStories';
import { IPage } from '../../interfaces/IPage';

const GamingPage: React.FC = () => {
    const [vg247News, setVg247News] = useState<IPage[]>([]);
    const [gamerantNews, setGamerantNews] = useState<IPage[]>([]);
    const [gameinformerNews, setGameinformerNews] = useState<IPage[]>([]);

    const fetchNews = async (): Promise<IStories> => {
        const responseRaw = await fetch('http://localhost:5000/gaming/all');
        const response = responseRaw.json();
        return response;
    };

    const setNews = async (): Promise<void> => {
        const news = await fetchNews();
        setVg247News(news.stories.vg247);
        setGamerantNews(news.stories.gamerant);
        setGameinformerNews(news.stories.gameinformer);
    };

    useEffect(() => {
        setNews();
    }, []);

    return (
        <article className="gaming-page">
            <div className="gaming-page__first-page">
                <List title="VG247" items={vg247News} />
            </div>
            <div className="gaming-page__second-page">
                <List title="Gamerant" items={gamerantNews} />
            </div>
            <div className="gaming-page__third-page">
                <List title="Gameinformer" items={gameinformerNews} />
            </div>
            <Link to="/" className="back-btn"><span>Back</span></Link>
        </article>
    );
};

export default GamingPage;
