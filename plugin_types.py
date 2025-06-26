from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class Mapping(BaseModel):
    key: str = Field(..., min_length=1)
    value: str
    multiline: Optional[bool] = None


class Action(BaseModel):
    key: Literal["exportCandidate"]
    label: str = Field(..., min_length=1)
    iconSvgBase64: str = Field(..., min_length=1)
    metaEndpoint: str = Field(..., min_length=1)
    mappings: Optional[List[Mapping]] = None


class ConfigurationFormField(BaseModel):
    key: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)
    actionKey: Optional[Literal["exportCandidate"]] = None
    defaultValue: Optional[str] = None
    type: Literal["string", "persisted_string"]
    placeholder: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    readonly: Optional[bool] = None
    sensitive: bool
    useAsHttpHeader: Optional[str] = Field(None, min_length=1)


class Schema(BaseModel):
    version: Literal["1.0.0"] = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    logoBase64: str = Field(..., min_length=1)
    actions: List[Action]
    configurationFormFields: Optional[List[ConfigurationFormField]] = None
    errorEndpoint: Optional[str] = None
