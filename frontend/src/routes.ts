import { RouteConfig } from 'react-router-config';
import LandingPage from './components/landingpage/LandingPage';
import NotFoundPage from './components/notfoundpage/NotFoundPage';

const routes: RouteConfig[] = [
    {
        component: LandingPage,
        exact: true,
        path: '/',
    },
    // {
    //     component: CategoryList,
    //     path: '/category/all',
    // },
    // {
    //     component: CategoryAdd,
    //     path: '/category/add',
    // },
    // {
    //     component: ExpenseList,
    //     path: '/expense/all',
    // },
    // {
    //     component: ExpenseAdd,
    //     path: '/expense/add',
    // },
    {
        component: NotFoundPage,
    },
];

export default routes;
