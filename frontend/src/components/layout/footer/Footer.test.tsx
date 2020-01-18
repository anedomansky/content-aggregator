import React from 'react';
import { shallow } from 'enzyme';
import Footer from './Footer';

// TODO: more tests!!
describe('Footer', () => {
    it('renders without crashing', () => {
        shallow(<Footer />);
    });
});
