import { IPage } from './IPage';

export interface INewsStories {
    stories: {
        'welt': IPage[];
        'spiegel': IPage[];
        'focus': IPage[];
    };
}
