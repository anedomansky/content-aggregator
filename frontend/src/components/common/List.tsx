import React from 'react';
import './List.scss';
import { IPage } from '../../interfaces/IPage';

interface Props {
    title: string;
    items: IPage[];
}

const List: React.FC<Props> = ({ title, items }) => (
    <article className="list">
        <h1 className="list__title">{title}</h1>
        <ul>
            {items.map((item: IPage, index: number) => (
                <li key={index}>
                    <a href={item.link} target="_blank" rel="noopener noreferrer">
                        <span>{item.snippet}</span>
                    </a>
                </li>
            ))}
        </ul>
    </article>
);

export default List;
