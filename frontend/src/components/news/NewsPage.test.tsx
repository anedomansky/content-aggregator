import React from 'react';
import { shallow } from 'enzyme';
import NewsPage from './Newspage';

// TODO: more tests!!
describe('Footer', () => {
    it('renders without crashing', () => {
        shallow(<NewsPage />);
    });
});
