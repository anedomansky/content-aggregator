import React from 'react';
import { shallow } from 'enzyme';
import NotFoundPage from './NotFoundPage';

// TODO: more tests!!
describe('Footer', () => {
    it('renders without crashing', () => {
        shallow(<NotFoundPage />);
    });
});
