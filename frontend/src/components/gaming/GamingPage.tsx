import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import List from '../common/List';
import './GamingPage.scss';
import { IGamingStories } from '../../interfaces/IGamingStories';
import { IPage } from '../../interfaces/IPage';

const GamingPage: React.FC = () => {
    const [vg247News, setVg247News] = useState<IPage[]>([]);
    const [gamerantNews, setGamerantNews] = useState<IPage[]>([]);
    const [gameinformerNews, setGameinformerNews] = useState<IPage[]>([]);
    const [loading, setLoading] = useState<boolean>(false);

    const fetchNews = async (): Promise<IGamingStories> => {
        const responseRaw = await fetch('http://localhost:5000/gaming/all');
        const response = responseRaw.json();
        return response;
    };

    const updateNews = async (): Promise<void> => {
        await fetch('http://localhost:5000/gaming/update?website=gamerant');
        await fetch('http://localhost:5000/gaming/update?website=gameinformer');
        await fetch('http://localhost:5000/gaming/update?website=vg247');
    };

    const setNews = async (): Promise<void> => {
        setLoading(true);
        await updateNews();
        const news = await fetchNews();
        setVg247News(news.stories.vg247);
        setGamerantNews(news.stories.gamerant);
        setGameinformerNews(news.stories.gameinformer);
        setLoading(false);
    };

    useEffect(() => {
        setNews();
    }, []);

    if (loading) {
        return (
            <article className="gaming-pagel--loading">Loading news. Please wait...</article>
        );
    }
    return (
        <article className="gaming-page">
            <button type="button" className="gaming-page__fetch-btn" onClick={setNews}>Fetch new stories?</button>
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
