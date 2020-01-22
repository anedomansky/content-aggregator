import { RouteConfig } from 'react-router-config';
import LandingPage from './components/landingpage/LandingPage';
import NotFoundPage from './components/notfoundpage/NotFoundPage';
import GamingPage from './components/gaming/GamingPage';
import NewsPage from './components/news/Newspage';

const routes: RouteConfig[] = [
    {
        component: LandingPage,
        exact: true,
        path: '/',
    },
    {
        component: GamingPage,
        path: '/gaming',
    },
    {
        component: NewsPage,
        path: '/news',
    },
    {
        component: NotFoundPage,
    },
];

export default routes;
