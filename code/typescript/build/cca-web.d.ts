import { GameDef } from './cca-lib';
export interface DisplayConfig {
    eleId?: string;
    width?: number;
    height?: number;
    entryPrompt?: string;
}
export declare function playGame(game: GameDef, displayCfg?: DisplayConfig): void;
