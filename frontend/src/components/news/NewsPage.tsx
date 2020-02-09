import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import List from '../common/List';
import './NewsPage.scss';
import { INewsStories } from '../../interfaces/INewsStories';
import { IPage } from '../../interfaces/IPage';

const NewsPage: React.FC = () => {
    const [weltNews, setWeltNews] = useState<IPage[]>([]);
    const [spiegelNews, setSpiegelNews] = useState<IPage[]>([]);
    const [focusNews, setFocusNews] = useState<IPage[]>([]);
    const [loading, setLoading] = useState<boolean>(false);

    const fetchNews = async (): Promise<INewsStories> => {
        const responseRaw = await fetch('http://localhost:5000/news/all');
        const response = responseRaw.json();
        return response;
    };

    const updateNews = async (): Promise<void> => {
        await fetch('http://localhost:5000/news/update?website=welt');
        await fetch('http://localhost:5000/news/update?website=spiegel');
        await fetch('http://localhost:5000/news/update?website=focus');
    };

    const setNews = async (): Promise<void> => {
        setLoading(true);
        await updateNews();
        const news = await fetchNews();
        setWeltNews(news.stories.welt);
        setSpiegelNews(news.stories.spiegel);
        setFocusNews(news.stories.focus);
        setLoading(false);
    };

    useEffect(() => {
        setNews();
    }, []);

    if (loading) {
        return (
            <article className="news-page--loading">
                <div className="news-page--loading__spinner" />
                <p>Loading news. Please wait...</p>
            </article>
        );
    }
    return (
        <article className="news-page" role="region">
            <button type="button" className="news-page__fetch-btn" onClick={setNews}>Fetch new stories?</button>
            <div className="news-page__first-page">
                <List title="Welt" items={weltNews} />
            </div>
            <div className="news-page__second-page">
                <List title="Spiegel" items={spiegelNews} />
            </div>
            <div className="news-page__third-page">
                <List title="Focus" items={focusNews} />
            </div>
            <Link to="/" className="back-btn"><span>Back</span></Link>
        </article>
    );
};

export default NewsPage;
